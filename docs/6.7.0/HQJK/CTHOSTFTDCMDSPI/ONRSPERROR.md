<p>针对用户请求的出错通知。</p>
<span class="anchor" id="6f76d817-a705-4558-b80d-105e0383d491"></span>
## 1.函数原型
<p>virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="08ea5498-9a4a-47dc-ae70-c85e8918d123"></span>
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
<span class="anchor" id="7b80169e-ace4-4db0-9df1-5eabf287faf7"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="5ad5f93f-4d72-402d-b99e-ec3fce9f0f1c"></span>
## 4.FAQ
<p>无</p>
