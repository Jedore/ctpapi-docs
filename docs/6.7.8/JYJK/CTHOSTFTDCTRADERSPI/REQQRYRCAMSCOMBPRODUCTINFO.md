<p>请求RCAMS产品组合信息查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRCAMSCOMBPRODUCTINFO/">OnRspQryRCAMSCombProductInfo</a></p>
<span class="anchor" id="dc931929-fdc6-4adf-9348-138dd74cc31b"></span>
## 1.函数原型
<p>virtual int ReqQryRCAMSCombProductInfo(CThostFtdcQryRCAMSCombProductInfoField *pQryRCAMSCombProductInfo, int nRequestID) = 0;</p>
<span class="anchor" id="67334f67-cfa4-455e-a7e4-9c7230fce7fd"></span>
## 2.参数
<p>pQryRCAMSCombProductInfo：RCAMS产品组合信息查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">ProductID</td>
<td style="TEXT-ALIGN: left;">产品代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">CombProductID</td>
<td style="TEXT-ALIGN: left;">商品组代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">ProductGroupID</td>
<td style="TEXT-ALIGN: left;">商品群代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<span class="anchor" id="af7af74f-7eb3-48e2-9dde-676bf2c0b6e2"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="388e7fab-9560-4854-9471-00fe87dddcbf"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="0bb9b760-c7bd-4526-98b3-109aecc290d6"></span>
## 5.FAQ
<p>无</p>
