<p>请求RCAMS空头期权风险调整参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRCAMSSHORTOPTADJUSTPARAM/">ReqQryRCAMSShortOptAdjustParam</a>后，该方法被调用。</p>
<span class="anchor" id="12e27b24-460f-4fec-9691-26085bc0fa5a"></span>
## 1.函数原型
<p>virtual void OnRspQryRCAMSShortOptAdjustParam(CThostFtdcRCAMSShortOptAdjustParamField *pRCAMSShortOptAdjustParam, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="7472f937-cef0-493e-852b-e588192d51ea"></span>
## 2.参数
<p>pRCAMSShortOptAdjustParam：RCAMS空头期权风险调整参数</p>
<pre><code>struct CThostFtdcRCAMSShortOptAdjustParamField
{
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///产品组合代码
    TThostFtdcProductIDType CombProductID;
    ///投套标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///空头期权风险调整标准
    TThostFtdcAdjustValueType   AdjustValue;
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
<span class="anchor" id="6ab11378-aede-4531-bb03-0d30eee2e94d"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="4fe41c8a-d8b6-4db3-ad1e-86052f8b7eff"></span>
## 4.FAQ
<p>无</p>
