<p>客户端认证响应,当执行<a href="../../CTHOSTFTDCTRADERSPI/REQAUTHENTICATE/">ReqAuthenticate</a>后，该方法被调用</p>
<span class="anchor" id="9acf51cf-fa75-4f66-b83f-ce46074c940d"></span>
## 1.函数原型
<p>virtual void OnRspAuthenticate(CThostFtdcRspAuthenticateField *pRspAuthenticateField, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="447ed633-39fd-4783-bc18-07fb54330f28"></span>
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
<span class="anchor" id="b43a94fa-2bf6-4040-b522-3328c3d178f6"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ab16d703-de6e-436a-98e5-e91b3c1c5253"></span>
## 4.FAQ
<p>无</p>
