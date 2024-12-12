<p>请求RCAMS同合约风险对冲参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRCAMSINSTRPARAMETER/">ReqQryRCAMSInstrParameter</a>后，该方法被调用。</p>
<span class="anchor" id="04f6d773-2807-42fc-9581-5fcd8c74db24"></span>
## 1.函数原型
<p>virtual void OnRspQryRCAMSInstrParameter(CThostFtdcRCAMSInstrParameterField *pRCAMSInstrParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="f0ad72d9-9fac-4f29-891f-e3466b665418"></span>
## 2.参数
<p>pRCAMSInstrParameter：RCAMS同合约风险对冲参数</p>
<pre><code>struct CThostFtdcRCAMSInstrParameterField
{
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///产品代码
    TThostFtdcProductIDType ProductID;
    ///同合约风险对冲比率
    TThostFtdcHedgeRateType HedgeRate;
};
</code></pre>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType   ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType  ErrorMsg;
};
</code></pre>
<span class="anchor" id="5e2ea05e-a70a-468d-a23e-65dac2dfd57f"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="4328bff1-85d3-4b4a-858f-a66741fb13eb"></span>
## 4.FAQ
<p>无</p>
