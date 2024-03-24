<p>客户端认证响应,当执行<a href="../../CTHOSTFTDCTRADERSPI/REQAUTHENTICATE/">ReqAuthenticate</a>后，该方法被调用</p>
<span class="anchor" id="d138259b-ac78-4df0-9a92-c32b348ed521"></span>
## 1.函数原型
<p>virtual void OnRspAuthenticate(CThostFtdcRspAuthenticateField *pRspAuthenticateField, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="38ed6e43-ad38-4953-bd6d-bc2a02f371bd"></span>
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
<span class="anchor" id="ff67f9e9-3804-4afd-9e93-0623ee7958a6"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="86f69cc7-f5e7-46db-b764-90926c9ef2e2"></span>
## 4.FAQ
<p>无</p>
