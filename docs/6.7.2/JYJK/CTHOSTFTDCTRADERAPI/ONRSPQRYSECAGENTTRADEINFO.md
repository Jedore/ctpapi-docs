<p>请求查询二级代理商信息响应</p>
<span class="anchor" id="3d5505b3-7a69-4799-bace-1e8a37fd0965"></span>
## 1.函数原型
<p>virtual void OnRspQrySecAgentTradeInfo(CThostFtdcSecAgentTradeInfoField *pSecAgentTradeInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="8c5882b9-ce0e-475e-b412-8b317d128a7c"></span>
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
<span class="anchor" id="7d552187-0cef-4328-a4ce-ae34a5b30c1c"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="753334c7-ba67-4ada-8412-5469fd5a12f6"></span>
## 4.FAQ
<p>无</p>
