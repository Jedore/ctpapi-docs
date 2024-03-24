<p>针对用户请求的出错通知。</p>
<span class="anchor" id="cb92eddf-247a-4b7d-aba3-90421ea54bc1"></span>
## 1.函数原型
<p>virtual void <a href="../../../JYJK/CTHOSTFTDCTRADERAPI/ONRSPERROR/">OnRspError</a>(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="a999e92c-b8b9-4546-8ec9-57556cb50f58"></span>
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
<span class="anchor" id="8a906d0d-f523-4176-a1c0-228c3b5d0a73"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="40c387f7-6fb4-4bff-8dc3-44c9c5e09ad4"></span>
## 4.FAQ
<p>无</p>
