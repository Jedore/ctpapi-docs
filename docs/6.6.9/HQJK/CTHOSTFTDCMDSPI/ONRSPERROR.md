<p>针对用户请求的出错通知。</p>
<span class="anchor" id="d1ab926e-6d58-42be-ac20-654d8ffad279"></span>
## 1.函数原型
<p>virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="598a3398-b35a-4656-b3e7-640e1e7e3daf"></span>
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
<span class="anchor" id="09249482-8fff-4090-bf9b-d51339297ea1"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="9a0fcedc-74eb-48ef-9c50-b33873ec3837"></span>
## 4.FAQ
<p>无</p>
