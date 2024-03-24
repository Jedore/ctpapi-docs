<p>查询用户当前支持的认证模式的回复</p>
<span class="anchor" id="bde77aa7-b001-4ce7-a3bb-35bc9edaa1d9"></span>
## 1.函数原型
<p>virtual void OnRspUserAuthMethod(CThostFtdcRspUserAuthMethodField *pRspUserAuthMethod, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="3e6f26ff-ab6e-4714-ae6a-4d819aad0e6b"></span>
## 2.参数
<p>pRspUserAuthMethod：用户发出获取安全安全登陆方法回复</p>
<pre><code>struct CThostFtdcRspUserAuthMethodField
{
    ///当前可以用的认证模式
    TThostFtdcCurrentAuthMethodType UsableAuthMethod;
};
</code></pre>
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
<span class="anchor" id="817caafa-2236-4bb5-bd34-84a74fc1adc4"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="499df84f-1c56-47c2-8aed-41688c468b5b"></span>
## 4.FAQ
<p>无</p>
