<p>针对用户请求的出错通知。</p>
<span class="anchor" id="247b6d88-ccc3-495b-ad88-3dff9b18bca4"></span>
## 1.函数原型
<p>virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="37446d9c-4d7d-4c25-b414-b42373da6792"></span>
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
<span class="anchor" id="c35f9602-f00c-496e-953c-ebc7e0d5376e"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="dca4d55e-6f81-4dda-8e3d-0429bcd9d4b5"></span>
## 4.FAQ
<p>无</p>
