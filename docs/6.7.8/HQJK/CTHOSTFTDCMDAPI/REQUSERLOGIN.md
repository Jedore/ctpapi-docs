<p>用户登录请求，对应响应<a href="../../CTHOSTFTDCMDSPI/ONRSPUSERLOGIN/">OnRspUserLogin</a>。目前行情登陆不校验账号密码。</p>
<span class="anchor" id="bc4e230f-3d71-496b-b334-e9e5bb0cce57"></span>
## 1.特别说明
<p>自CTP交易系统升级6.6.2版本后，后台支持对用户登录行情前置进行身份校验。</p>
<p>若启用该功能后，登录行情前置时要求当前交易日该IP已成功登录过交易系统，且发起登录行情的请求中必须正确填写BrokerID和UserID，与登录交易的信息保持一致。</p>
<p>不填、填错或该IP未成功登录过交易系统，则校验不通过，会提示“CTP:不合法登录”；</p>
<p>若不启用，则无需验证，可直接发起登录。</p>
<span class="anchor" id="dea45d3a-e1ff-4a24-b784-f69163be90be"></span>
## 2.函数原型
<p>virtual int <a href="../../../JYJK/CTHOSTFTDCTRADERSPI/REQUSERLOGIN/">ReqUserLogin</a>(CThostFtdc<a href="../../../JYJK/CTHOSTFTDCTRADERSPI/REQUSERLOGIN/">ReqUserLogin</a>Field *p<a href="../../../JYJK/CTHOSTFTDCTRADERSPI/REQUSERLOGIN/">ReqUserLogin</a>Field, int nRequestID) = 0;</p>
<span class="anchor" id="db75fa46-a9e6-4abb-af84-72e639f83677"></span>
## 3.参数
<p>p<a href="../../../JYJK/CTHOSTFTDCTRADERSPI/REQUSERLOGIN/">ReqUserLogin</a>Field：用户登录请求</p>
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
<p>CTP后台用户事件中的用户登录事件所显示的用户端产品信息取自ReqAuthentication接口里的UserProductInfo，而非<a href="../../../JYJK/CTHOSTFTDCTRADERSPI/REQUSERLOGIN/">ReqUserLogin</a>里的。</p>
</blockquote>
<p>LoginRemark：可以写登录备注，能够被交易系统的日志查询到。</p>
<p>IPAddress：系统自动获取，填写无效。</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="8017e6b7-e13f-4998-9268-0a38b804f009"></span>
## 4.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="0d7a633e-91b7-4ca2-b813-d553490388dc"></span>
## 5.调用示例
<pre><code>CThostFtdcReqUserLoginField reqUserLogin = {0};
m_pUserMdApi-&gt;ReqUserLogin(&amp;reqUserLogin, nRequestID++);
</code></pre>
<span class="anchor" id="4f13207b-1186-4341-87c1-7cb08d8b715d"></span>
## 6.FAQ
<p>无</p>
