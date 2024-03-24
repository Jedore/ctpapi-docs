<p>请求查询分类合约响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYCLASSIFIEDINSTRUMENT/">ReqQryClassifiedInstrument</a>后，该方法被调用。</p>
<span class="anchor" id="0861bf93-01eb-4174-b5d0-5bac8ae78fdd"></span>
## 1.函数原型
<p>virtual void OnRspQryClassifiedInstrument(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="1782de70-4fb2-44f8-b1de-1a777d77640a"></span>
## 2.参数
<p>pInstrument：合约</p>
<pre><code>struct CThostFtdcInstrumentField
{
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///合约名称
    TThostFtdcInstrumentNameType    InstrumentName;
    ///保留的无效字段
    TThostFtdcOldExchangeInstIDType reserve2;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve3;
    ///产品类型
    TThostFtdcProductClassType  ProductClass;
    ///交割年份
    TThostFtdcYearType  DeliveryYear;
    ///交割月
    TThostFtdcMonthType DeliveryMonth;
    ///市价单最大下单量
    TThostFtdcVolumeType    MaxMarketOrderVolume;
    ///市价单最小下单量
    TThostFtdcVolumeType    MinMarketOrderVolume;
    ///限价单最大下单量
    TThostFtdcVolumeType    MaxLimitOrderVolume;
    ///限价单最小下单量
    TThostFtdcVolumeType    MinLimitOrderVolume;
    ///合约数量乘数
    TThostFtdcVolumeMultipleType    VolumeMultiple;
    ///最小变动价位
    TThostFtdcPriceType PriceTick;
    ///创建日
    TThostFtdcDateType  CreateDate;
    ///上市日
    TThostFtdcDateType  OpenDate;
    ///到期日
    TThostFtdcDateType  ExpireDate;
    ///开始交割日
    TThostFtdcDateType  StartDelivDate;
    ///结束交割日
    TThostFtdcDateType  EndDelivDate;
    ///合约生命周期状态
    TThostFtdcInstLifePhaseType InstLifePhase;
    ///当前是否交易
    TThostFtdcBoolType  IsTrading;
    ///持仓类型
    TThostFtdcPositionTypeType  PositionType;
    ///持仓日期类型
    TThostFtdcPositionDateTypeType  PositionDateType;
    ///多头保证金率
    TThostFtdcRatioType LongMarginRatio;
    ///空头保证金率
    TThostFtdcRatioType ShortMarginRatio;
    ///是否使用大额单边保证金算法
    TThostFtdcMaxMarginSideAlgorithmType    MaxMarginSideAlgorithm;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve4;
    ///执行价
    TThostFtdcPriceType StrikePrice;
    ///期权类型
    TThostFtdcOptionsTypeType   OptionsType;
    ///合约基础商品乘数
    TThostFtdcUnderlyingMultipleType    UnderlyingMultiple;
    ///组合类型
    TThostFtdcCombinationTypeType   CombinationType;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///合约在交易所的代码
    TThostFtdcExchangeInstIDType    ExchangeInstID;
    ///产品代码
    TThostFtdcInstrumentIDType  ProductID;
    ///基础商品代码
    TThostFtdcInstrumentIDType  UnderlyingInstrID;
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
<span class="anchor" id="abdae0fd-fd50-4496-8efe-2f7a43260b4d"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="db2928aa-df78-45b3-acb2-0580aa8b38c9"></span>
## 4.FAQ
<p>无</p>
