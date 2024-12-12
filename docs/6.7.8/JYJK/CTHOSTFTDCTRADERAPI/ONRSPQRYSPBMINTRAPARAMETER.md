<p>请求SPBM品种内对锁仓折扣参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMINTRAPARAMETER/">ReqQrySPBMIntraParameter</a>后，该方法被调用。</p>
<span class="anchor" id="95ab85b5-83f4-4a09-9567-2c6138671524"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMIntraParameter(CThostFtdcSPBMIntraParameterField *pSPBMIntraParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="49cb9b19-1178-4b21-93e7-2dfcf7cf166d"></span>
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
<span class="anchor" id="ee77b4c3-2deb-4ac3-84cd-d6f58f6fcb91"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="9f584177-aba1-472c-8c6b-66edde20e617"></span>
## 4.FAQ
<p>无</p>
