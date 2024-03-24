<p>用户登录请求，对应响应OnRspUserLogin。目前行情登陆不校验账号密码。</p>
<span class="anchor" id="b590097e-a9ad-46c9-8367-f0f97964f87a"></span>
## 1.函数原型
<p>virtual int ReqUserLogin(CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID) = 0;</p>
<span class="anchor" id="0261ff54-acc6-4f76-adf4-58183617ed2a"></span>
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
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="224a6736-44cf-4ce0-9d54-0b161f1111db"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="3d7162e6-dbaf-44d9-bde2-0d6522a95a1f"></span>
## 4.调用示例
<pre><code>CThostFtdcReqUserLoginField reqUserLogin = {0};
m_pUserMdApi-&gt;ReqUserLogin(&amp;reqUserLogin, nRequestID++);
</code></pre>
<span class="anchor" id="c5aab546-15af-4c9f-92d2-e0b123f1d20a"></span>
## 5.FAQ
<p>无</p>
