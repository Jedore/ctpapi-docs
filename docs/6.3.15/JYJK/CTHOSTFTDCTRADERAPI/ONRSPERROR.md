<p>针对用户请求的出错通知。</p>
<span class="anchor" id="ecf1c96a-0ece-48aa-8465-99c229794f95"></span>
## 1.函数原型
<p>virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="76da613e-7624-407b-8bbe-2407f5619c52"></span>
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
<span class="anchor" id="7516f5cb-0545-4828-9564-0da9a7f3c7ee"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="e82feaaf-373b-4c3e-9fc1-93fe7a3e4fca"></span>
## 4.FAQ
<p><div class="region_i" id=""><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">查询时遇到报“OnRspError[90]: CTP：查询未就绪，请稍后重试”</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>可能此时查询核心还没有就绪，建议稍后再做一次查询操作。此类情况一般发生在用户登录后立即发起查询，建议登录后隔一秒再查询。</p>
<p>还有一种情况就是遇到前置流控了，<a href="../../../QTYWGZ/LK/">报单流控、查询流控和会话数控制</a>。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
