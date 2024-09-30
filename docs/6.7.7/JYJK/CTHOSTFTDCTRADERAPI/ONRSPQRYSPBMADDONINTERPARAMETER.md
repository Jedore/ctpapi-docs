<p>请求SPBM附加跨品种抵扣参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMADDONINTERPARAMETER/">ReqQrySPBMAddOnInterParameter</a>后，该方法被调用。</p>
<span class="anchor" id="21b60f25-0fe1-42ad-8d52-43633c64794b"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMAddOnInterParameter(CThostFtdcSPBMAddOnInterParameterField *pSPBMAddOnInterParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="dde1350f-9e5a-4159-bdc8-2a2e4addb6d1"></span>
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
<span class="anchor" id="ca608369-585b-48a6-9c02-5331ae646299"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="19080f29-6270-43ad-b260-d52b16ff92fe"></span>
## 4.FAQ
<p>无</p>
