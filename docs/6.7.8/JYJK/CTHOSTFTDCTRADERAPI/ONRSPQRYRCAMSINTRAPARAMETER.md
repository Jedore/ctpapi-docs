<p>请求RCAMS品种内风险对冲参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRCAMSINTRAPARAMETER/">ReqQryRCAMSIntraParameter</a>后，该方法被调用。</p>
<span class="anchor" id="f621d553-c0f5-4308-8dd3-39a26f2d0d9c"></span>
## 1.函数原型
<p>virtual void OnRspQryRCAMSIntraParameter(CThostFtdcRCAMSIntraParameterField *pRCAMSIntraParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="f45e1f52-c37b-4892-8b45-e78c8bc2d0fe"></span>
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
<span class="anchor" id="7c5aab78-31e6-4a6a-842a-8ce830c41f64"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="d67e94ee-3ede-451a-9cf1-c9fbab498657"></span>
## 4.FAQ
<p>无</p>
