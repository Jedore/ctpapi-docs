<p>请求查询二级代理商信息响应</p>
<span class="anchor" id="bd55265a-afc0-4e07-ad14-945143a4d1d5"></span>
## 1.函数原型
<p>virtual void OnRspQrySecAgentTradeInfo(CThostFtdcSecAgentTradeInfoField *pSecAgentTradeInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="0a94abf0-1d8a-49f7-8446-f9e0a5c21abd"></span>
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
<span class="anchor" id="a281ed56-400b-4442-91fc-e80e84a0adf7"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="b741bc61-83d6-4eb4-861a-276edcd246ac"></span>
## 4.FAQ
<p>无</p>
