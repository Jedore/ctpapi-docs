<p>针对用户请求的出错通知。</p>
<span class="anchor" id="00d1eac1-5bf6-489e-bb94-78196108195c"></span>
## 1.函数原型
<p>virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="50c2509f-399d-46cc-aad2-9bc42c072636"></span>
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
<span class="anchor" id="76674df5-b257-4847-bcef-e282f8847b11"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="c0b53305-cc33-4a1b-95d3-4b8b34029e99"></span>
## 4.FAQ
<p>无</p>
