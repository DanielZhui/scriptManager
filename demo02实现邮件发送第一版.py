from selenium import webdriver
import time

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
driver.find_element_by_xpath('//*[@id="account-box"]/div[2]/input').send_keys('msmezh63')
time.sleep(1)
# 输入密码(变量)
driver.find_element_by_xpath('//*[@id="login-form"]/div[1]/div[3]/div[2]/input[2]').send_keys('zxc123')
driver.save_screenshot('login01.png')
# driver
# 点击登录
driver.find_element_by_xpath('//*[@id="dologin"]').click()


# 由于账号没有绑定手机号这里会在动态加载一个页面(继续登录)，需等待加载才能登录
# 这里由于网速问题可能导致报错所以最好延时等待久一点

time.sleep(6)
driver.save_screenshot('login02.png')
driver.find_element_by_xpath('//*[@id="cnt-box2"]/div/div[2]/div[3]/a[1]').click()
# 切换回主文档
driver.switch_to.default_content()
# 等待新页面加载成功
time.sleep(10)

# # 点击写信
driver.find_element_by_xpath("//b[@class='nui-ico fn-bg ga0']").click()
driver.save_screenshot('login03.png')
#
# 点击写信之后等待页面被加载完成
time.sleep(5)
# 定位收件人 输入收件人(变量)
receiver = driver.find_element_by_xpath("//div[@class='js-component-emailinput nui-addr nui-editableAddr nui-editableAddr-edit']/input")
time.sleep(1)
receiver.send_keys('msmezh24@126.com')

time.sleep(1)
theme = driver.find_element_by_xpath("//div[@class='kZ0 fu0']/div[1]/div/div/input")
# 定位主题(变量)
theme.send_keys('召开信息：2019.5月-长沙—前三届已经EI检索')

time.sleep(1)
# # 定位到切换源码(源码变量)
driver.find_element_by_xpath("//b[@class='ico ico-editor ico-editor-source']").click()
# # 发送主题
time.sleep(1)
text = driver.find_element_by_xpath("//textarea[@class='APP-editor-textarea']")

file = open('101.html', mode='r')
for line in file:
    text.send_keys(line)

# html测试
# text.send_keys("<h2>hello world</h2>")

driver.save_screenshot('login04.png')

time.sleep(2)
# 点击发送按钮
driver.find_element_by_xpath("//footer[@class='jp0']/div[1]/span[2]").click()
print('发送成功')
