<p>请求查询交易编码响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYTRADINGCODE/">ReqQryTradingCode</a>后，该方法被调用。</p>
<span class="anchor" id="6b2c0c35-6ef9-46bb-b15d-0960aa572b94"></span>
## 1.函数原型
<p>virtual void OnRspQryTradingCode(CThostFtdcTradingCodeField *pTradingCode, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="5b2dc535-aa6e-47f8-804c-f9feb9914bb9"></span>
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
<span class="anchor" id="78c68ccc-31dc-410f-bf68-476606ad2170"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="e5a48324-ace5-4fc6-9380-033ea2fba764"></span>
## 4.FAQ
<p>无</p>
