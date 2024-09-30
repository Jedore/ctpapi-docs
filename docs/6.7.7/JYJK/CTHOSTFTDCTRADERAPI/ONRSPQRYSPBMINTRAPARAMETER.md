<p>请求SPBM品种内对锁仓折扣参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMINTRAPARAMETER/">ReqQrySPBMIntraParameter</a>后，该方法被调用。</p>
<span class="anchor" id="3bb0bc13-1bfe-4b18-b7f1-ddbebd262bec"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMIntraParameter(CThostFtdcSPBMIntraParameterField *pSPBMIntraParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="7254a2c5-b025-4ccc-85d9-2dff1a5ac124"></span>
## 2.参数
<p>pSPBMIntraParameter：SPBM品种内对锁仓折扣参数</p>
<pre><code>struct CThostFtdcSPBMIntraParameterField
{
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///品种代码
    TThostFtdcInstrumentIDType  ProdFamilyCode;
    ///品种内合约间对锁仓费率折扣比例
    TThostFtdcRatioType IntraRateY;
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
<span class="anchor" id="4a279095-94bb-46ff-8898-d5d97563eaae"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="beaa1d4c-1e40-408f-add5-0615348221c4"></span>
## 4.FAQ
<p>无</p>
