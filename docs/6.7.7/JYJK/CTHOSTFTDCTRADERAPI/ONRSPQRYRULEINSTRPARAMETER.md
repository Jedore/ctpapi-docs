<p>请求RULE合约保证金参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRULEINSTRPARAMETER/">ReqQryRULEInstrParameter</a>后，该方法被调用。</p>
<span class="anchor" id="b8f36535-afd2-4198-9cef-f498d623e83d"></span>
## 1.函数原型
<p>virtual void OnRspQryRULEInstrParameter(CThostFtdcRULEInstrParameterField *pRULEInstrParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="ac43ccc4-d830-46de-828a-d2dd0d2e6d1c"></span>
## 2.参数
<p>pRULEInstrParameter：RULE合约保证金参数</p>
<pre><code>struct CThostFtdcRULEInstrParameterField
{
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///合约类型
    TThostFtdcInstrumentClassType   InstrumentClass;
    ///标准合约
    TThostFtdcInstrumentIDType  StdInstrumentID;
    ///投机买折算系数
    TThostFtdcRatioType BSpecRatio;
    ///投机卖折算系数
    TThostFtdcRatioType SSpecRatio;
    ///套保买折算系数
    TThostFtdcRatioType BHedgeRatio;
    ///套保卖折算系数
    TThostFtdcRatioType SHedgeRatio;
    ///买附加风险保证金
    TThostFtdcMoneyType BAddOnMargin;
    ///卖附加风险保证金
    TThostFtdcMoneyType SAddOnMargin;
    ///商品群号
    TThostFtdcCommodityGroupIDType  CommodityGroupID;
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
<span class="anchor" id="d6ed1416-6729-4dd5-ae10-4a424e757635"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="c8d7a890-b45a-4827-bd50-811df3fb67fe"></span>
## 4.FAQ
<p>无</p>
