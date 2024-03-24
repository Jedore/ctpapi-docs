<p>用户登录请求，对应响应<a href="../../CTHOSTFTDCMDSPI/ONRSPUSERLOGIN/">OnRspUserLogin</a>。目前行情登陆不校验账号密码。</p>
<span class="anchor" id="e062f7c3-5f13-4c68-9692-baca29e688bb"></span>
## 1.特别说明
<p>自CTP交易系统升级6.6.2版本后，后台支持对用户登录行情前置进行身份校验。</p>
<p>若启用该功能后，登录行情前置时要求当前交易日该IP已成功登录过交易系统，且发起登录行情的请求中必须正确填写BrokerID和UserID，与登录交易的信息保持一致。</p>
<p>不填、填错或该IP未成功登录过交易系统，则校验不通过，会提示“CTP:不合法登录”；</p>
<p>若不启用，则无需验证，可直接发起登录。</p>
<span class="anchor" id="f650d0dd-8326-48aa-ac47-1ea89ba7bca6"></span>
## 2.函数原型
<p>virtual int ReqUserLogin(CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID) = 0;</p>
<span class="anchor" id="cba3787c-e3ed-478a-8a6c-61934ebbd221"></span>
## 3.参数
<p>pReqUserLoginField：用户登录请求</p>
<pre><code>struct CThostFtdcReqUserLoginField
{
    ///交易日
    TThostFtdcDateType TradingDay;
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///密码
    TThostFtdcPasswordType Password;
    ///用户端产品信息
    TThostFtdcProductInfoType UserProductInfo;
    ///接口端产品信息
    TThostFtdcProductInfoType InterfaceProductInfo;
    ///协议信息
    TThostFtdcProtocolInfoType ProtocolInfo;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
    ///动态密码
    TThostFtdcPasswordType OneTimePassword;
    ///终端IP地址
    TThostFtdcIPAddressType ClientIPAddress;
    ///登录备注
    TThostFtdcLoginRemarkType LoginRemark;
};
</code></pre>
<p>BrokerID:开启行情身份校验功能后，该字段必需正确填写</p>
<p>UserID：操作员代码，后续请求中的investorid需要属于该操作员的组织架构下；开启行情身份校验功能后，该字段必需正确填写</p>
<p>UserProductInfo：客户端的产品信息，如软件开发商、版本号等，</p>
<blockquote>
<p>CTP后台用户事件中的用户登录事件所显示的用户端产品信息取自ReqAuthentication接口里的UserProductInfo，而非ReqUserLogin里的。</p>
</blockquote>
<p>LoginRemark：可以写登录备注，能够被交易系统的日志查询到。</p>
<p>IPAddress：手工填写本机IP地址，不自动获取。填写规则如下：ipv4原样填写，ipv6要转成非零压缩地址，即原始地址，同时要去掉冒号，eg：AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="d26c3603-f82b-4d7b-96dd-3c259aaa9cda"></span>
## 4.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="91e1f936-4889-4881-8cef-70b5645effbc"></span>
## 5.调用示例
<pre><code>CThostFtdcReqUserLoginField reqUserLogin = {0};
m_pUserMdApi-&gt;ReqUserLogin(&amp;reqUserLogin, nRequestID++);
</code></pre>
<span class="anchor" id="5e52249e-ca96-433b-a327-5f81719f93e8"></span>
## 6.FAQ
<p>无</p>
