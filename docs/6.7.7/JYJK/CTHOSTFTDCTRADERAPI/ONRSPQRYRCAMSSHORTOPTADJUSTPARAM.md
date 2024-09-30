<p>请求RCAMS空头期权风险调整参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRCAMSSHORTOPTADJUSTPARAM/">ReqQryRCAMSShortOptAdjustParam</a>后，该方法被调用。</p>
<span class="anchor" id="cd13471e-0046-4b1e-94ab-736c8fc6e9e3"></span>
## 1.函数原型
<p>virtual void OnRspQryRCAMSShortOptAdjustParam(CThostFtdcRCAMSShortOptAdjustParamField *pRCAMSShortOptAdjustParam, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="bd9cff49-50ab-436d-a744-a9fd023427af"></span>
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
<span class="anchor" id="0d955eba-443f-4efb-a77c-d78032a9e810"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="6f0fdbe5-9a31-4aed-9e59-d0c252677f0b"></span>
## 4.FAQ
<p>无</p>
