<p>请求RCAMS品种内风险对冲参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRCAMSINTRAPARAMETER/">ReqQryRCAMSIntraParameter</a>后，该方法被调用。</p>
<span class="anchor" id="d6f38e11-be2a-488a-9b0a-f36177e5404c"></span>
## 1.函数原型
<p>virtual void OnRspQryRCAMSIntraParameter(CThostFtdcRCAMSIntraParameterField *pRCAMSIntraParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="da1b920d-5137-4a40-b26b-1996b491048e"></span>
## 2.参数
<p>pRCAMSIntraParameter：RCAMS品种内风险对冲参数</p>
<pre><code>struct CThostFtdcRCAMSIntraParameterField
{
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///产品组合代码
    TThostFtdcProductIDType CombProductID;
    ///品种内对冲比率
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
<span class="anchor" id="6cec079f-eb00-47a9-be2b-e66270ab116e"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="a6d8f1e7-9846-4bc8-b247-d4a4bcd244b0"></span>
## 4.FAQ
<p>无</p>
