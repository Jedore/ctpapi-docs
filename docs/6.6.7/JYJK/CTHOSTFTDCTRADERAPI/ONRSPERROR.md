<p>针对用户请求的出错通知。</p>
<span class="anchor" id="0247f1e9-c3ff-445f-9ba2-8b482eceb8cf"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDSPI/ONRSPERROR/">OnRspError</a>(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="2b35d472-92b6-41d4-b10a-7f7d7011fc5e"></span>
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
<span class="anchor" id="f14b856e-6ba1-4120-a18f-5b4d25dbf056"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="77959adb-e3eb-44ff-92be-a728146f1d65"></span>
## 4.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">查询时遇到报“<a href="../../../HQJK/CTHOSTFTDCMDSPI/ONRSPERROR/">OnRspError</a>[90]: CTP：查询未就绪，请稍后重试”</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>可能此时查询核心还没有就绪，建议稍后再做一次查询操作。此类情况一般发生在用户登录后立即发起查询，建议登录后隔一秒再查询。</p>
<p>还有一种情况就是遇到前置流控了，<a href="../../../QTYWGZ/LK/">报单流控、查询流控和会话数控制</a>。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
