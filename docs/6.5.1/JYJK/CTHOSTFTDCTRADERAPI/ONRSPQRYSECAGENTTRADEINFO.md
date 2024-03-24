<p>请求查询二级代理商信息响应</p>
<span class="anchor" id="365a2927-e0ca-46fc-8bcc-57879eeb6e8e"></span>
## 1.函数原型
<p>virtual void OnRspQrySecAgentTradeInfo(CThostFtdcSecAgentTradeInfoField *pSecAgentTradeInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="273dc477-b5db-49ba-b7f4-16b3a5100e90"></span>
## 2.参数
<p>pSecAgentTradeInfo：二级代理商信息</p>
<pre><code>struct CThostFtdcSecAgentTradeInfoField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///境外中介机构资金帐号
    TThostFtdcAccountIDType BrokerSecAgentID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///二级代理商姓名
    TThostFtdcLongIndividualNameType LongCustomerName;
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
<span class="anchor" id="980104c0-4269-4312-8c85-4095b2755352"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="68634b1f-18fb-43e3-bd14-d0552eb60779"></span>
## 4.FAQ
<p>无</p>
