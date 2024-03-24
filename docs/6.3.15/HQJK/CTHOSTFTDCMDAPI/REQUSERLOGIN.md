<p>用户登录请求，对应响应OnRspUserLogin。目前行情登陆不校验账号密码。</p>
<span class="anchor" id="dba642cc-7c56-4b6a-bb4f-60daacfb7b73"></span>
## 1.函数原型
<p>virtual int ReqUserLogin(CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID) = 0;</p>
<span class="anchor" id="3571e39b-83ee-4eb6-9c54-83525570d24b"></span>
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
<p>例如：SFITTraderV100。</p>
</blockquote>
<p>LoginRemark：可以写登录备注，能够被交易系统的日志查询到。</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="43fa3ede-07c1-45ec-be10-9fc5100b0609"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="0b03188c-6443-4bd3-9112-928f9a967fe5"></span>
## 4.调用示例
<pre><code>CThostFtdcReqUserLoginField reqUserLogin = {0};
m_pUserMdApi-&gt;ReqUserLogin(&amp;reqUserLogin, nRequestID++);
</code></pre>
<span class="anchor" id="ac366516-4476-40db-a14d-e83a618f9ce2"></span>
## 5.FAQ
<p>无</p>
