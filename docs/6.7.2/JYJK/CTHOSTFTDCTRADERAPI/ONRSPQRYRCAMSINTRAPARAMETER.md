<p>请求RCAMS品种内风险对冲参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRCAMSINTRAPARAMETER/">ReqQryRCAMSIntraParameter</a>后，该方法被调用。</p>
<span class="anchor" id="334cf2d4-2748-4ff9-a457-2e1269cd16e5"></span>
## 1.函数原型
<p>virtual void OnRspQryRCAMSIntraParameter(CThostFtdcRCAMSIntraParameterField *pRCAMSIntraParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="8db8f431-ef77-44b7-b4c0-6d6e6ac19bcc"></span>
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
<span class="anchor" id="c95f7da5-577f-45b5-a60e-bda3171249bc"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="0d9e60f4-2580-4ba4-a467-baa24efdc2d6"></span>
## 4.FAQ
<p>无</p>
