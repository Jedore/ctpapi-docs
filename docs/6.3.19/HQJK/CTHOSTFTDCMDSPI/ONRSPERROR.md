<p>针对用户请求的出错通知。</p>
<span class="anchor" id="56a6f9a4-ba07-441b-a5c8-7c0d22b89aaf"></span>
## 1.函数原型
<p>virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="3fe5ca89-f314-4574-aad9-1a3ba40d9c03"></span>
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
<span class="anchor" id="cd583443-f0e9-47d0-a30b-341668bef806"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="fddcf4c1-dd8f-4def-8b1d-9784320430f3"></span>
## 4.FAQ
<p>无</p>
