<p>请求RCAMS产品组合信息查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRCAMSCOMBPRODUCTINFO/">ReqQryRCAMSCombProductInfo</a>后，该方法被调用。</p>
<span class="anchor" id="d0317761-026a-4b52-9812-3c206bb9bfe5"></span>
## 1.函数原型
<p>virtual void <a href="../ONRSPQRYSPBMADDONINTERPARAMETER/">OnRspQrySPBMAddOnInterParameter</a>(CThostFtdcSPBMAddOnInterParameterField *pSPBMAddOnInterParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="b84fc1e2-1d75-43fb-93df-474751dcf0aa"></span>
## 2.参数
<p>pSPBMAddOnInterParameter：SPBM附加跨品种抵扣参数</p>
<pre><code>struct CThostFtdcSPBMAddOnInterParameterField
{
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///优先级
    TThostFtdcSpreadIdType  SpreadId;
    ///品种间对锁仓附加费率折扣比例
    TThostFtdcRatioType AddOnInterRateZ2;
    ///第一腿构成品种
    TThostFtdcInstrumentIDType  Leg1ProdFamilyCode;
    ///第二腿构成品种
    TThostFtdcInstrumentIDType  Leg2ProdFamilyCode;
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
<span class="anchor" id="9b085249-56bb-4875-a8ba-b840cf55855c"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="8acecb06-5261-4489-be8c-ed64e7aaa9c8"></span>
## 4.FAQ
<p>无</p>
