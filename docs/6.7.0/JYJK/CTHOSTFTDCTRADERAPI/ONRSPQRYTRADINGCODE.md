<p>请求查询交易编码响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYTRADINGCODE/">ReqQryTradingCode</a>后，该方法被调用。</p>
<span class="anchor" id="ed7ceac1-a1fb-4a54-9fa3-1f08bc4774c9"></span>
## 1.函数原型
<p>virtual void OnRspQryTradingCode(CThostFtdcTradingCodeField *pTradingCode, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="050d1f5e-a6bd-4c0e-90fa-042e42396002"></span>
## 2.参数
<p>pTradingCode：交易编码</p>
<pre><code>struct CThostFtdcTradingCodeField
{
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///客户代码
    TThostFtdcClientIDType ClientID;
    ///是否活跃
    TThostFtdcBoolType IsActive;
    ///交易编码类型
    TThostFtdcClientIDTypeType ClientIDType;
    ///营业部编号
    TThostFtdcBranchIDType BranchID;
    ///业务类型
    TThostFtdcBizTypeType BizType;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
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
<span class="anchor" id="dc3b863a-8c2b-4c9d-9197-a67ee20b3ffb"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="294089f1-4101-4a84-9419-f09fe2b0d53a"></span>
## 4.FAQ
<p>无</p>
