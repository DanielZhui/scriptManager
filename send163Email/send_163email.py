import time,random
from selenium import webdriver



class Base(object):
    '''基本类'''

    def __init__(self):
        self.susername = open('superemail/126.txt', mode='r')
        self.yeahname = open('superemail/yeah.txt', mode='r')
        self.pwd = 'xxxxx'
        # 收件人
        self.receiver = open('superemail/text.txt', mode='r')
        # 126账号发送错误账号记录
        self.error_txt = open('superemail/error.txt', mode='a+')
        # yeah账号发送错误账号记录
        self.error1_txt = open('superemail/error2.txt', mode='a+')

        # 将126发件人和收件人打包成一一对应的结构
        self.res = zip(self.susername, self.receiver)
        # 将yeah发件人和收件人打包一一对应
        self.res1 = zip(self.yeahname, self.receiver)
        # 主题怎么放？
        # 将主题添加到列表中随机取出
        self.theme_list = []
        self.all_theme = open('superemail/主题.txt', mode='r')
        for theme in self.all_theme:
            self.theme_list.append(theme)

        # 模板列表
        self.temp_list = []
        for i in range(101, 121):
            s = 'superemail/模板/' + str(i) + '.html'
            self.temp_list.append(s)
        self.temp = random.choice(self.temp_list)

class Send123(Base):

    @staticmethod
    def send123(self):
        ''''
        进入循环
        sname：126发件人
        rec：收件人
        error_txt:发送失败的账号
        theme_list:主题列表
        temp:模板列表
        '''
        for sname,rec in self.res:
            driver = webdriver.Firefox()
            url = 'https://email.163.com/'
            driver.get(url)

            # 获取126邮箱登录组件
            ename = driver.find_element_by_xpath('//*[@id="nav"]/li[2]/b')
            ename.click()

            # 休眠10秒等待组件被加载完毕
            time.sleep(6)

            # 切换到组件里
            login_iframe = driver.find_element_by_xpath('//*[@id="panel-126"]/iframe')
            driver.switch_to.frame(login_iframe)
            time.sleep(1)

            # 输入账户(变量)
            driver.find_element_by_xpath('//*[@id="account-box"]/div[2]/input').send_keys(sname)
            time.sleep(1)
            # 输入密码(变量)
            driver.find_element_by_xpath('//*[@id="login-form"]/div[1]/div[3]/div[2]/input[2]').send_keys("zxc123")
            driver.save_screenshot('login01.png')

            # 点击登录
            driver.find_element_by_xpath('//*[@id="dologin"]').click()

            # 由于账号没有绑定手机号这里会在动态加载一个页面(继续登录)，需等待加载才能登录
            # 这里由于网速问题可能导致报错所以最好延时等待久一点
            try:
                time.sleep(6)
                driver.find_element_by_xpath('//*[@id="cnt-box2"]/div/div[2]/div[3]/a[1]').click()
                # 切换回主文档
                driver.switch_to.default_content()
                # 等待新页面加载成功
                time.sleep(10)

                # # 点击写信
                driver.find_element_by_xpath("//b[@class='nui-ico fn-bg ga0']").click()
                # 点击写信之后等待页面被加载完成
                time.sleep(5)
                # 定位收件人 输入收件人(变量)
                receiver = driver.find_element_by_xpath(
                    "//div[@class='js-component-emailinput nui-addr nui-editableAddr nui-editableAddr-edit']/input")
                time.sleep(1)
                receiver.send_keys(rec)

                time.sleep(1)
                theme = driver.find_element_by_xpath("//div[@class='kZ0 fu0']/div[1]/div/div/input")
                ### 发送主题 随机在主题列表中取出一个主题 ####
                print(random.choice(self.theme_list))
                theme.send_keys(random.choice(self.theme_list))

                time.sleep(1)
                # # 定位到切换源码(源码变量)
                driver.find_element_by_xpath("//b[@class='ico ico-editor ico-editor-source']").click()
                # # 发送主题
                time.sleep(1)
                ### 切换到文本框(随机取出一个模板) ###
                text = driver.find_element_by_xpath("//textarea[@class='APP-editor-textarea']")

                choice_temp = random.choice(self.temp_list)
                print('>>>>>>>>',choice_temp)
                file = open(choice_temp,mode='r')
                for line in file:
                    text.send_keys(line)


                time.sleep(2)
                # 点击发送按钮
                driver.find_element_by_xpath("//footer[@class='jp0']/div[1]/span[2]").click()
                print('>>>>>%s发送成功' %(sname.strip()))
                time.sleep(2)


            except:
                # 发送失败的账号（出现图片验证码的）
                driver.save_screenshot("%s.png" %sname)
                self.error_txt.write(sname)
                print('>>>>>%s发送失败' %(sname.strip()))
            driver.close()


class yeahemail(Base):

    @staticmethod
    def sendyeah(self):
        ''''
        进入循环
        sname：126发件人
        rec：收件人
        error_txt:发送失败的账号
        theme_list:主题列表
        temp:模板列表
        '''
        for yeah,rec in self.res:
            print('???????????')
            driver = webdriver.Firefox()
            url = 'https://email.163.com/'
            driver.get(url)

            # 获取126邮箱登录组件
            ename = driver.find_element_by_xpath('//*[@id="nav"]/li[3]/b')
            ename.click()

            # 休眠10秒等待组件被加载完毕
            time.sleep(6)

            # 切换到组件里
            login_iframe = driver.find_element_by_xpath('//*[@id="panel-yeah"]/iframe')
            driver.switch_to.frame(login_iframe)
            time.sleep(1)

            # 输入账户(变量)
            driver.find_element_by_xpath('//*[@id="account-box"]/div[2]/input').send_keys(yeah)
            time.sleep(1)
            # 输入密码(变量)
            driver.find_element_by_xpath('//*[@id="login-form"]/div[1]/div[3]/div[2]/input[2]').send_keys("zxc123")

            # 点击登录
            driver.find_element_by_xpath('//*[@id="dologin"]').click()

            # 由于账号没有绑定手机号这里会在动态加载一个页面(继续登录)，需等待加载才能登录
            # 这里由于网速问题可能导致报错所以最好延时等待久一点
            try:
                time.sleep(6)
                driver.find_element_by_xpath('//*[@id="cnt-box2"]/div/div[2]/div[3]/a[1]').click()
                # 切换回主文档
                driver.switch_to.default_content()
                # 等待新页面加载成功
                time.sleep(10)

                # # 点击写信
                driver.find_element_by_xpath("//*[@id='_mail_component_24_24']").click()
                #
                # 点击写信之后等待页面被加载完成
                time.sleep(5)
                # 定位收件人 输入收件人(变量)
                receiver = driver.find_element_by_xpath(
                    "//div[@class='js-component-emailinput nui-addr nui-editableAddr nui-editableAddr-edit']/input")
                time.sleep(1)
                receiver.send_keys(rec)

                time.sleep(1)
                theme = driver.find_element_by_xpath("//div[@class='kZ0 fu0']/div[1]/div/div/input")
                ### 发送主题 随机在主题列表中取出一个主题 ####
                theme.send_keys(random.choice(self.theme_list))

                time.sleep(1)
                # # 定位到切换源码(源码变量)
                driver.find_element_by_xpath("//b[@class='ico ico-editor ico-editor-source']").click()
                # # 发送主题
                time.sleep(1)
                ### 切换到文本框(随机取出一个模板) ###
                text = driver.find_element_by_xpath("//textarea[@class='APP-editor-textarea']")

                choice_temp = random.choice(self.temp_list)
                file = open(choice_temp,mode='r')
                for line in file:
                    text.send_keys(line)


                time.sleep(2)
                # 点击发送按钮
                driver.find_element_by_xpath("//footer[@class='jp0']/div[1]/span[2]").click()
                print('>>>>>%s发送成功' %(yeah.strip()))
                time.sleep(2)
                driver.close()

            except:
                # 发送失败的账号（出现图片验证码的）
                driver.save_screenshot('%s.png' %yeah)
                self.error1_txt.write(yeah)
                print('>>>>>%s发送失败' %(yeah.strip()))
                driver.close()
                
if __name__ == '__main__':
    '''项目启动入口'''
    Send123.send123()
    yeahemail.sendyeah()
