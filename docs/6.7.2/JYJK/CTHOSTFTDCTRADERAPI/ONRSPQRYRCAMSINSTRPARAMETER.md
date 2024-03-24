<p>请求RCAMS同合约风险对冲参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRCAMSINSTRPARAMETER/">ReqQryRCAMSInstrParameter</a>后，该方法被调用。</p>
<span class="anchor" id="fe0be65b-5b02-4f5c-98af-4c8348709ba8"></span>
## 1.函数原型
<p>virtual void OnRspQryRCAMSInstrParameter(CThostFtdcRCAMSInstrParameterField *pRCAMSInstrParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="2195633b-18c1-49d2-a70c-d25cadfcf2a9"></span>
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
<span class="anchor" id="be8d1e0d-a3dd-4df0-9b2d-6c6751afd594"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="6740ff3b-2117-43f1-81a0-a8dd71e5346d"></span>
## 4.FAQ
<p>无</p>
