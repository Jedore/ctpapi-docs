<p>客户端认证响应,当执行<a href="../../CTHOSTFTDCTRADERSPI/REQAUTHENTICATE/">ReqAuthenticate</a>后，该方法被调用</p>
<span class="anchor" id="ad1e96d6-7e5d-417c-a70d-402ff6a8d184"></span>
## 1.函数原型
<p>virtual void OnRspAuthenticate(CThostFtdcRspAuthenticateField *pRspAuthenticateField, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="1b4c332d-c787-4861-a9ad-47158d828751"></span>
## 2.参数
<p>pRspAuthenticateField：客户端认证响应</p>
<pre><code>struct CThostFtdcRspAuthenticateField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///用户端产品信息
    TThostFtdcProductInfoType UserProductInfo;
    ///App代码
    TThostFtdcAppIDType AppID;
    ///App类型
    TThostFtdcAppTypeType AppType;
};
</code></pre>
<p>UserProductInfo：客户端的产品信息，如软件开发商、版本号等。</p>
<blockquote>
<p>例如：SFITTraderV100。</p>
</blockquote>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="44dde144-3af2-477c-bb25-3a642716339f"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="e2072f0b-a592-4a49-aa51-4d936dad5a4c"></span>
## 4.FAQ
<p>无</p>
