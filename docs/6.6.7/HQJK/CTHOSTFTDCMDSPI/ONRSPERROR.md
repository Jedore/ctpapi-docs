<p>针对用户请求的出错通知。</p>
<span class="anchor" id="a55f4d9f-9acd-424d-a605-0e58deeb62d9"></span>
## 1.函数原型
<p>virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="3dc934b5-d48b-4f3c-abfc-2c7cd9af9596"></span>
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
<span class="anchor" id="bdf66af8-9a2e-4529-9d9f-19f6d88765aa"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="0d6307c4-aaf3-4dc2-9b75-c935787ef177"></span>
## 4.FAQ
<p>无</p>
