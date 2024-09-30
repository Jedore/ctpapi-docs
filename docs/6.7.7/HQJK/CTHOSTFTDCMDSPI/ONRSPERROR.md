<p>针对用户请求的出错通知。</p>
<span class="anchor" id="6a7d5596-2366-45d7-a6d7-71435c8c3a41"></span>
## 1.函数原型
<p>virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="f37e8fbb-1d52-48f4-b43e-b97494d43a6d"></span>
## 2.参数
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
<span class="anchor" id="f2579225-04a8-4f6a-a203-637913f053e3"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="749b499d-8c63-4e18-b931-2a0cb6e7eb0f"></span>
## 4.FAQ
<p>无</p>
