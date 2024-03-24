<p>请求查询二级代理商信息响应</p>
<span class="anchor" id="84c2d96f-1faa-4bb3-a3d0-d11bf04d6083"></span>
## 1.函数原型
<p>virtual void OnRspQrySecAgentTradeInfo(CThostFtdcSecAgentTradeInfoField *pSecAgentTradeInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="a7abd2b9-09e0-4c69-9720-ef2a2d7f36bf"></span>
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
<span class="anchor" id="babd0c68-2bc5-45a1-8f9f-469fc40bd724"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="901c679c-51c9-485a-8b19-816e4c6eeef2"></span>
## 4.FAQ
<p>无</p>
