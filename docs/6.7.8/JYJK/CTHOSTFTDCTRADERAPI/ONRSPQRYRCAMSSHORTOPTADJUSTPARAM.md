<p>请求RCAMS空头期权风险调整参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRCAMSSHORTOPTADJUSTPARAM/">ReqQryRCAMSShortOptAdjustParam</a>后，该方法被调用。</p>
<span class="anchor" id="9767ad18-8745-4532-a81f-d4ef59a30cfe"></span>
## 1.函数原型
<p>virtual void OnRspQryRCAMSShortOptAdjustParam(CThostFtdcRCAMSShortOptAdjustParamField *pRCAMSShortOptAdjustParam, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="6e481043-c8dc-4918-896e-855a09daf9ec"></span>
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
<span class="anchor" id="2d7faaef-a243-45fe-a6f4-725b23e230e2"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="8855907f-3b3a-49fa-ada6-4556ed4bb046"></span>
## 4.FAQ
<p>无</p>
