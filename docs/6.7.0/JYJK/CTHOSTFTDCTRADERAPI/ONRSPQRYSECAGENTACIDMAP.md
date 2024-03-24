<p>请求查询二级代理操作员银期权限响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSECAGENTACIDMAP/">ReqQrySecAgentACIDMap</a>后，该方法被调用。</p>
<span class="anchor" id="225d23fa-7eb5-49c2-a854-a2e65c3e7f00"></span>
## 1.函数原型
<p>virtual void OnRspQrySecAgentACIDMap(CThostFtdcSecAgentACIDMapField *pSecAgentACIDMap, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="851544ff-0525-4cf5-bb73-3b2509141e7f"></span>
## 2.参数
<p>pSecAgentACIDMap：二级代理操作员银期权限</p>
<pre><code>struct CThostFtdcSecAgentACIDMapField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///资金账户
    TThostFtdcAccountIDType AccountID;
    ///币种
    TThostFtdcCurrencyIDType CurrencyID;
    ///境外中介机构资金帐号
    TThostFtdcAccountIDType BrokerSecAgentID;
};
</code></pre>
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
<span class="anchor" id="f7dce50e-a498-402d-910d-71c58ed035a8"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ce5cdfd5-3eb2-42d4-910e-53e48f70129c"></span>
## 4.FAQ
<p>无</p>
