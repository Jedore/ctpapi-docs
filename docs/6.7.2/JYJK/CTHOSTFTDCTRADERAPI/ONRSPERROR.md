<p>针对用户请求的出错通知。</p>
<span class="anchor" id="e3f6161e-118b-432f-9011-5357775e0e27"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDSPI/ONRSPERROR/">OnRspError</a>(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="f6cecb5d-7a61-4505-b479-3ebb0a54abf5"></span>
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
<span class="anchor" id="5a829afd-4367-4d51-a6b3-adf04697b545"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="8c8b7fab-a58c-4c19-bd20-685f03df75e9"></span>
## 4.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">查询时遇到报“<a href="../../../HQJK/CTHOSTFTDCMDSPI/ONRSPERROR/">OnRspError</a>[90]: CTP：查询未就绪，请稍后重试”</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>可能此时查询核心还没有就绪，建议稍后再做一次查询操作。此类情况一般发生在用户登录后立即发起查询，建议登录后隔一秒再查询。</p>
<p>还有一种情况就是遇到前置流控了，<a href="../../../QTYWGZ/LK/">报单流控、查询流控和会话数控制</a>。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
