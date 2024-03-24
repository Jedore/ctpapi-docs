<p>针对用户请求的出错通知。</p>
<span class="anchor" id="d38ae7e2-5edd-41b9-a51e-225d5cde3c85"></span>
## 1.函数原型
<p>virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="3d420901-9b4f-4591-9084-c4467b984f71"></span>
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
<span class="anchor" id="d9ec651e-04ca-46f7-a204-cd1705f0e915"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="459292b1-745d-4da4-80d0-3b4aab4b16f3"></span>
## 4.FAQ
<p>无</p>
