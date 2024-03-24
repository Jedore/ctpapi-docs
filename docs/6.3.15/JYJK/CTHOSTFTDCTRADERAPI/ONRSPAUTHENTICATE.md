<p>客户端认证响应,当执行ReqAuthenticate后，该方法被调用</p>
<span class="anchor" id="d4d367f4-44d6-449e-a1f6-cbe20a81f092"></span>
## 1.函数原型
<p>virtual void OnRspAuthenticate(CThostFtdcRspAuthenticateField *pRspAuthenticateField, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="c28a1aa8-6d91-457b-abfc-0f0528ce1ad6"></span>
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
<span class="anchor" id="0b39f998-fb24-40f2-93f4-f9e22bf84c09"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="4005a083-243e-4347-a619-cce9bddc10e8"></span>
## 4.FAQ
<p>无</p>
