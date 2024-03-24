<p>请求SPBM品种内对锁仓折扣参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMINTRAPARAMETER/">ReqQrySPBMIntraParameter</a>后，该方法被调用。</p>
<span class="anchor" id="b11389ad-3c0c-4de8-8af0-a91e33dcb14d"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMIntraParameter(CThostFtdcSPBMIntraParameterField *pSPBMIntraParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="13abdf8e-3f17-4f83-babc-4b5ece5803b9"></span>
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
<span class="anchor" id="c036e915-9e5c-4153-8569-2ff6db4627b0"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="36c77b62-202b-43e3-992f-06264d98b660"></span>
## 4.FAQ
<p>无</p>
