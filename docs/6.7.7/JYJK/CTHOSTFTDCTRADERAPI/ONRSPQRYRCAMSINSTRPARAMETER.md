<p>请求RCAMS同合约风险对冲参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRCAMSINSTRPARAMETER/">ReqQryRCAMSInstrParameter</a>后，该方法被调用。</p>
<span class="anchor" id="bbb49b9e-7ffc-47a1-ab8e-da4d35d8fcc8"></span>
## 1.函数原型
<p>virtual void OnRspQryRCAMSInstrParameter(CThostFtdcRCAMSInstrParameterField *pRCAMSInstrParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="58ee4fb2-8e2e-42e2-955a-0453c765be8f"></span>
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
<span class="anchor" id="e8f7cca8-254e-4baf-9ac7-b9ba311adee7"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="920367b4-e9ec-4a4b-9ee4-24e53c3c8162"></span>
## 4.FAQ
<p>无</p>
