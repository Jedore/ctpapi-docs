<p>请求SPBM跨品种抵扣参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMINTERPARAMETER/">ReqQrySPBMInterParameter</a>后，该方法被调用。</p>
<span class="anchor" id="8ed8ed7f-7846-4c60-ab78-b4c216b2b42b"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMInterParameter(CThostFtdcSPBMInterParameterField *pSPBMInterParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="d03103ad-fea3-4a34-b46f-1fc93bd9e9e8"></span>
## 2.参数
<p>pSPBMInterParameter：SPBM跨品种抵扣参数</p>
<pre><code>struct CThostFtdcSPBMInterParameterField
{
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///优先级
    TThostFtdcSpreadIdType  SpreadId;
    ///品种间对锁仓费率折扣比例
    TThostFtdcRatioType InterRateZ;
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
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<span class="anchor" id="8378ae77-d9e6-42a9-8ba0-ebaf78f56490"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="68e3b559-c166-4cec-aa14-725ff702e342"></span>
## 4.FAQ
<p>无</p>
