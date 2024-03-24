<p>请求SPBM品种内对锁仓折扣参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMINTRAPARAMETER/">ReqQrySPBMIntraParameter</a>后，该方法被调用。</p>
<span class="anchor" id="45e43602-d39b-45fd-8b3e-3e858bea6ac3"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMIntraParameter(CThostFtdcSPBMIntraParameterField *pSPBMIntraParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="ac02d360-4252-4c61-83f4-71953ba20166"></span>
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
<span class="anchor" id="d7841801-5ba6-419b-ab65-007dec98a967"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="8c817a13-ddf9-4b25-81d1-d30e3179ed26"></span>
## 4.FAQ
<p>无</p>
