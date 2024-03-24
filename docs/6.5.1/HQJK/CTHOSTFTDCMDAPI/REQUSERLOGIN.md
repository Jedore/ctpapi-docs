<p>用户登录请求，对应响应OnRspUserLogin。目前行情登陆不校验账号密码。</p>
<span class="anchor" id="de190ff5-4194-48a1-a93a-644184ca73c3"></span>
## 1.函数原型
<p>virtual int ReqUserLogin(CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID) = 0;</p>
<span class="anchor" id="bb6368c0-a58e-4b07-9808-86a97c36c0a3"></span>
## 2.参数
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
<p>UserID：操作员代码，后续请求中的investorid需要属于该操作员的组织架构下。</p>
<p>UserProductInfo：客户端的产品信息，如软件开发商、版本号等，</p>
<blockquote>
<p>CTP后台用户事件中的用户登录事件所显示的用户端产品信息取自ReqAuthentication接口里的UserProductInfo，而非ReqUserLogin里的。</p>
</blockquote>
<p>LoginRemark：可以写登录备注，能够被交易系统的日志查询到。</p>
<p>IPAddress：手工填写本机IP地址，不自动获取。填写规则如下：ipv4原样填写，ipv6要转成非零压缩地址，即原始地址，同时要去掉冒号，eg：AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="8d12eb15-ffa8-4cff-a1d7-894a77e0927f"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="26f5fca4-11ce-4d23-b9d2-7fcca77011cc"></span>
## 4.调用示例
<pre><code>CThostFtdcReqUserLoginField reqUserLogin = {0};
m_pUserMdApi-&gt;ReqUserLogin(&amp;reqUserLogin, nRequestID++);
</code></pre>
<span class="anchor" id="939e56c4-da3b-4a17-a61b-224ac7f26ebd"></span>
## 5.FAQ
<p>无</p>
