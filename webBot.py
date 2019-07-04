from selenium import webdriver

#site da Amazon usado como exemplo
browser = webdriver.Chrome('/home/silas/DEV/python/webBot/chromedriver') #caminho do arquivo executavel para o google chrome
#site que será aberto
browser.get('https://www.amazon.com.br/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com.br%2F%3Ftag%3Dhydrbrabk-20%26hvadid%3D336865328556%26hvpos%3D1t1%26hvnetw%3Dg%26hvrand%3D12377528052177922330%26hvpone%3D%26hvptwo%3D%26hvqmt%3Db%26hvdev%3Dc%26hvdvcmdl%3D%26hvlocint%3D%26hvlocphy%3D1001511%26hvtargid%3Dkwd-31326321%26ref%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=brflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

#elem = browser.find_element_by_link_text("Download")
#elem.click()

#searchBar = browser.find_element_by_id('q')
#searchBar.send_keys('Donwload')

#aqui, manipulamos e interagimos com o dom do site

email = browser.find_element_by_id('ap_email')
email.send_keys('email')

senha = browser.find_element_by_id('ap_password')
senha.send_keys('password')

#clique na checkbox de relembrar senha
checkbox = browser.find_element_by_name('rememberMe')
checkbox.click()

#botão de login
login = browser.find_element_by_id('signInSubmit')
login.click()


#mandando dados para a searchbar 
searchBar = browser.find_element_by_id('twotabsearchtextbox')
searchBar.send_keys('macbook pro 15')

#clicando no boto de pesquisa
submit = browser.find_element_by_class_name('nav-input')
submit.click()










