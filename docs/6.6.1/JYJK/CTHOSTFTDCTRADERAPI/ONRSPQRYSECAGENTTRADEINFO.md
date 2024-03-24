<p>请求查询二级代理商信息响应</p>
<span class="anchor" id="9d92d194-5141-4b7d-95d5-dbe28f6e2f93"></span>
## 1.函数原型
<p>virtual void OnRspQrySecAgentTradeInfo(CThostFtdcSecAgentTradeInfoField *pSecAgentTradeInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="bc6fcbed-18eb-47d5-b1f2-b1ff60edfc91"></span>
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
<span class="anchor" id="02ca7fc7-789e-4073-9953-c20f02d44bcd"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="9deb56c2-d09a-41dd-b0fc-2401a9133fc4"></span>
## 4.FAQ
<p>无</p>
