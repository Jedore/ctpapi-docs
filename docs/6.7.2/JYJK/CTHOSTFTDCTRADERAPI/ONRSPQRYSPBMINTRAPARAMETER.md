<p>请求SPBM品种内对锁仓折扣参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMINTRAPARAMETER/">ReqQrySPBMIntraParameter</a>后，该方法被调用。</p>
<span class="anchor" id="83347038-76b3-4cf0-82a2-5e7d8af34217"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMIntraParameter(CThostFtdcSPBMIntraParameterField *pSPBMIntraParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="ad4fd54e-95fd-444e-903f-05e326a0b287"></span>
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
<span class="anchor" id="4a9a1ab4-5c66-4d7a-9bcf-d1b3c2e15e80"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="5af05c2d-32c8-4202-8d93-d84ca45bc571"></span>
## 4.FAQ
<p>无</p>
