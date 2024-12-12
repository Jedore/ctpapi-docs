<p>针对用户请求的出错通知。</p>
<span class="anchor" id="c406fe39-9a4b-420e-a9fb-b9f244bc06c0"></span>
## 1.函数原型
<p>virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="6be56560-c9a5-4cc7-86e8-a508d7984c25"></span>
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
<span class="anchor" id="ca8d8b8e-f4f6-4fac-8ab7-eddd2c2242a5"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="b4a22cbd-f986-4107-82aa-5c11ec64b86d"></span>
## 4.FAQ
<p>无</p>
